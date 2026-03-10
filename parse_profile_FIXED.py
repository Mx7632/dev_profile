#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse profile.md to JSON"""
import re, json
from pathlib import Path
from datetime import datetime

def extract_section(content, title):
   pattern = rf"## {title}(.*?)(?=## |$)"
   match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ""

def parse_basic(section):
    if not section: return {}
   patterns = {
        'name': r'\*\*姓名 \(Name\):\*\*\s*(.+)',
        'role': r'\*\*职位 \(Role\):\*\*\s*(.+)',
        'greeting': r'\*\*标语 \(Greeting\):\*\*\s*(.+)',
        'bio': r'\*\*简介 \(Bio\):\*\*\s*(.+)',
        'status': r'\*\*状态 \(Status\):\*\*\s*(.+)',
        'avatar': r'\*\*头像路径 \(Profile Photo\):\*\*\s*(.+)'
    }
    info = {}
    for k, p in patterns.items():
       m = re.search(p, section)
        info[k] = m.group(1).strip() if m else ""
    return info

def parse_contact(section):
    if not section: return {}
   patterns = {
        'email': r'\*\*Email:\*\*\s*(.+)',
        'github': r'\*\*GitHub:\*\*\s*(.+)',
        'blog': r'\*\*Blog:\*\*\s*(.+)'
    }
   contact = {}
    for k, p in patterns.items():
        m = re.search(p, section)
       contact[k] = m.group(1).strip() if m else ""
    return contact

def parse_about(section):
    if not section: return {}
    about = {}
    m = re.search(r'\*\*学历 \(Education\):\*\*\s*(.+)', section)
    about['education'] = m.group(1).strip() if m else ""
    highlights = re.findall(r'-\s+(\d+.*?)$', section, re.MULTILINE)
    about['highlights'] = highlights[:5]
    desc_start = section.find("**详细描述 (Description):**")
    if desc_start != -1:
        desc = section[desc_start + len("**详细描述 (Description):**"):].strip()
        desc = re.sub(r'\n\s*\n', '\n\n', desc).strip()
        about['description'] = desc
    else:
        about['description'] = ""
    return about

def parse_projects(section):
    if not section: return []
   projects= []
    blocks = re.split(r'### Project \d+:', section)[1:]
   colors = [
        'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
        'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
        'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)'
    ]
    for idx, block in enumerate(blocks, 1):
       proj = {'id': idx, 'name': '', 'type': '', 'description': '', 'solution': '', 'techStack': [], 'icon': 'fa-code', 'color': colors[idx % len(colors)]}
        for line in block.strip().split('\n'):
            line = line.strip()
            if line.startswith('- **类型:**'): proj['type'] = line.replace('- **类型:**', '').strip()
            elif line.startswith('- **描述:**'): proj['description'] = line.replace('- **描述:**', '').strip()
            elif line.startswith('- **难点与方案:**'): proj['solution'] = line.replace('- **难点与方案:**', '').strip()
            elif line.startswith('- **技术栈:**'): proj['techStack'] = [t.strip() for t in line.replace('- **技术栈:**', '').split(',')]
        if block.strip().split('\n'):
           name_line = block.strip().split('\n')[0].strip()
            if ':' in name_line: name_line = name_line.split(':', 1)[0]
           proj['name'] = name_line
       projects.append(proj)
    return projects

def parse_skills(section):
    if not section: return []
    skills = []
    categories = [('编程语言', 'fa-code'), ('数据库', 'fa-database'), ('框架与中间件', 'fa-server'), ('DevOps & 工具', 'fa-tools'), ('其他标签', 'fa-tags')]
   color_map = {
        'Java': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'Python': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
        'Go': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
        'MySQL': 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
        'Redis': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'
    }
    for cat_name, icon in categories:
        cat_pattern = f"### {cat_name}"
        cat_start = section.find(cat_pattern)
        if cat_start == -1: continue
        next_cat = section.find("###", cat_start + 1)
        cat_content = section[cat_start:] if next_cat == -1 else section[cat_start:next_cat]
        items = []
        for m in re.finditer(r'-\s+\*\*(.+?):\*\*\s+(\d+)%', cat_content):
            skill_name = m.group(1).strip()
            level = int(m.group(2))
            items.append({'name': skill_name, 'level': level, 'color': color_map.get(skill_name, '')})
        if cat_name == '其他标签':
            tags_line = cat_content.split('\n')[-1].strip()
            if tags_line.startswith('- '):
                tags_text = tags_line[2:]
                tags = [t.strip() for t in tags_text.split(',')]
                for tag in tags:
                    if tag and not any(item['name'] == tag for item in items):
                        items.append({'name': tag, 'level': 60, 'color': ''})
        if items:
            skills.append({'name': cat_name, 'icon': icon, 'items': items})
    return skills

def main():
   print("=" * 60)
   print("🚀 Profile Markdown 解析器")
   print("=" * 60)
   print()
    md_path = Path("profile.md")
    if not md_path.exists():
       print(f"❌ 错误：找不到文件 {md_path}")
        return 1
   with open(md_path, 'r', encoding='utf-8') as f:
       content = f.read()
    try:
       print("📖 正在解析 profile.md...")
        data = {
            'meta': {'version': '1.0.0', 'generatedAt': datetime.now().isoformat(), 'source': str(md_path)},
            'basic': parse_basic(extract_section(content, "1. 基础信息")),
            'contact': parse_contact(extract_section(content, "2. 联系方式")),
            'about': parse_about(extract_section(content, "3. 关于我")),
            'projects': parse_projects(extract_section(content, "4. 项目经历")),
            'skills': parse_skills(extract_section(content, "5. 技术栈"))
        }
       print("💾 正在生成 JSON 文件...")
       output_path = Path("src/data/profile.json")
       output_path.parent.mkdir(parents=True, exist_ok=True)
       with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
       print()
       print("=" * 60)
       print("✅ 解析完成！")
       print("=" * 60)
       print(f"📊 数据统计:")
       print(f"   - 基本信息：✓")
       print(f"   - 联系方式：✓")
       print(f"   - 关于我：✓")
       print(f"   - 项目数量：{len(data['projects'])}")
       print(f"   - 技能类别：{len(data['skills'])}")
       print()
       print(f"📁 输出文件：{output_path}")
       print()
       print("🎉 现在可以在前端中使用这些数据了！")
       print("=" * 60)
    except Exception as e:
       print(f"❌ 解析失败：{e}")
       import traceback
        traceback.print_exc()
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
