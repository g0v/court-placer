import csv, json

out_dict = {}
out_dict2 = {}
with open('./地方法院管轄區域.csv', newline='') as src_csv:
    reader = csv.DictReader(src_csv)
    for row in reader:
        if row['地方法院'] not in out_dict:
            out_dict[row['地方法院']] = {}

        out_dict[row['地方法院']][row['簡易庭']] = {}
        loc_array = row['鄉鎮區'].split('、')
        now_city = ""
        for loc in loc_array:
            now_town = loc
            if len(loc) > 5:
                now_city = loc[0:3]
                now_town = loc[3:]
            if now_city not in out_dict[row['地方法院']][row['簡易庭']]:
                out_dict[row['地方法院']][row['簡易庭']][now_city] = []
            out_dict[row['地方法院']][row['簡易庭']][now_city].append(now_town)
            out_dict2[now_town] = {
                "city": now_city,
                "sim": row['簡易庭'],
                "court": row['地方法院']
            }

with open('./地方法院管轄區域.json', 'w', newline='') as out_json:
    out_json.write(json.dumps(out_dict, ensure_ascii=False))
with open('./鄉鎮區對應法院.json', 'w', newline='') as out_json:
    out_json.write(json.dumps(out_dict2, ensure_ascii=False))