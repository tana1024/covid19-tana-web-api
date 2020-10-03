# covid19-tana-web-api
[![LICENSE](https://img.shields.io/github/license/tana1024/covid19-tana-web-api?color=blue)](./LICENSE)

都道府県ごとの最新のCOVID-19（コロナウイルス）情報を取得するWeb APIです。(個人利用用です。)

#  使い方

* [Prefectures](#prefectures)

## 都道府県ごとのデータ(Prefectures)

**Endpoint**: [https://covid19-tana-web-api-git-master.tana1024.vercel.app/api/v1/prefectures](https://covid19-tana-web-api-git-master.tana1024.vercel.app//api/v1/prefectures)

<details>
<summary><b>Response</b></summary>

```json
[
  {
    "id": "1",
    "latest": "2020/09/25",
    "prefectureNameJ": "北海道",
    "prefectureNameE": "Hokkaido",
    "testedPositive": "2007",
    "peopleTested": "54736.0",
    "hospitalized": "97.0",
    "serious": "1",
    "discharged": "1803.0",
    "deaths": "107",
    "effectiveReproductionNumber": "1.61"
  },
...
```

</details>

---
