#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re

# Comprehensive 308-Scam Dataset Builder for IsThisScamOrReal.com
# Covering: Wikipedia, FBI IC3, FTC, Action Fraud UK, I4C India, Scamwatch Australia, Canadian Anti-Fraud Centre, Interpol, Google News 2026

scams = []

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text

def add(name, year, is_latest, country, cat, cat_slug, cat_name, score, desc, sample, source, kaise, flags, actions, icon="⚠️"):
    sid = slugify(f"{name}-{year}")
    scams.append({
        "id": sid,
        "slug": sid,
        "icon": icon,
        "name": name,
        "year": year,
        "isLatest": is_latest,
        "country": country,
        "category": cat,
        "categorySlug": cat_slug,
        "categoryName": cat_name,
        "score": score,
        "desc": desc,
        "sampleMsg": sample,
        "source": source,
        "kaiseHotaHai": kaise,
        "redFlags": flags,
        "kyaKarein": actions
    })

print("Starting to load data...")
