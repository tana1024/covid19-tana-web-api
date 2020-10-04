# covid19-tana-web-api
[![LICENSE](https://img.shields.io/github/license/tana1024/covid19-tana-web-api?color=blue)](./LICENSE)

最新のCOVID-19（コロナウイルス）の各種情報を取得するWeb APIです。(個人利用用です。)

#  使い方

* [Death Daily](#death-daily)：日次の死者数を取得する。
* [Prefectures](#prefectures)：都道府県ごとのCOVID-19に関する各種データを取得する。

## Death Daily

**Endpoint**: [https://covid19-tana-web-api-git-master.tana1024.vercel.app/api/v1/death_daily](https://covid19-tana-web-api-git-master.tana1024.vercel.app//api/v1/death_daily)

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


## Prefectures

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
