# Full Scampedia 308 Scams Generator
import json

scams = []

def scam(sid, name, year, is_latest, country, category, category_slug, category_name, score, desc, sample, source, kaise, flags, actions, icon='⚠️'):
    scams.append({
        'id': sid,
        'slug': sid,
        'icon': icon,
        'name': name,
        'year': year,
        'isLatest': is_latest,
        'country': country,
        'category': category,
        'categorySlug': category_slug,
        'categoryName': category_name,
        'score': score,
        'desc': desc,
        'sampleMsg': sample,
        'source': source,
        'kaiseHotaHai': kaise,
        'redFlags': flags,
        'kyaKarein': actions
    })
