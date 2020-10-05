# covid19-tana-web-api
[![LICENSE](https://img.shields.io/github/license/tana1024/covid19-tana-web-api?color=blue)](./LICENSE)

最新のCOVID-19（コロナウイルス）の各種情報を取得するWeb APIです。(個人利用用です。)

#  使い方

* [Death Daily](#death-daily)：日次の死者数を取得する。
* [Effective Reproduction](#effective-reproduction)：日次の実効再生産数を取得する。
* [PCR Positive Daily](#pcr-positive-daily)：日次のPCR検査陽性の人数を取得する。
* [PCR Tested Daily](#pcr-tested-daily)：日次のPCR検査数を取得する。
* [Prefectures](#prefectures)：都道府県ごとのCOVID-19に関する各種データを取得する。
* [Serious](#serious)：その日の重傷者の人数を取得する。

## Death Daily

**Endpoint**: [https://covid19-tana-web-api-git-master.tana1024.vercel.app/api/v1/death_daily](https://covid19-tana-web-api-git-master.tana1024.vercel.app/api/v1/death_daily)

<details>
<summary><b>Response</b></summary>

```json
[
  {
     date: "2020/02/14",
     death: "1"
  },
  ...
]
```
|項目|内容|
|----|--------|
|date|対象日付|
|death|死亡者数|

</details>

---

## Effective Reproduction

**Endpoint**: [https://covid19-tana-web-api-git-master.tana1024.vercel.app/api/v1/effective_reproduction](https://covid19-tana-web-api-git-master.tana1024.vercel.app//api/v1/effective_reproduction)

<details>
<summary><b>Response</b></summary>

```json
[
  {
    date: "2020/03/01",
    effective_reproduction: "1.22"
  },
  ...
]
```
|項目|内容|
|----|--------|
|date|対象日付|
|death|実効再生産数|

</details>

---

## PCR Positive Daily

**Endpoint**: [https://covid19-tana-web-api-git-master.tana1024.vercel.app/api/v1/pcr_positive_daily](https://covid19-tana-web-api-git-master.tana1024.vercel.app//api/v1/pcr_positive_daily)

<details>
<summary><b>Response</b></summary>

```json
[
  {
    date: "2020/01/16",
    pcr_positive: "1"
  },
  ...
]
```
|項目|内容|
|----|--------|
|date|対象日付|
|pcr_positive|PCRの陽性者数|

</details>

---

## PCR Tested Daily

**Endpoint**: [https://covid19-tana-web-api-git-master.tana1024.vercel.app/api/v1/pcr_tested_daily](https://covid19-tana-web-api-git-master.tana1024.vercel.app//api/v1/pcr_tested_daily)

<details>
<summary><b>Response</b></summary>

```json
[
  {
    date: "2020/02/05",
    pcr_tested: "4"
  },
  ...
]
```
|項目|内容|
|----|--------|
|date|対象日付|
|pcr_tested|PCR検査数|

</details>

---

## Prefectures

**Endpoint**: [https://covid19-tana-web-api-git-master.tana1024.vercel.app/api/v1/prefectures](https://covid19-tana-web-api-git-master.tana1024.vercel.app//api/v1/prefectures)

<details>
<summary><b>Response</b></summary>

```json
[
  {
    id: "1",
    latest: "2020/10/03",
    prefectureNameJ: "北海道",
    prefectureNameE: "Hokkaido",
    testedPositive: "2141",
    peopleTested: "58835.0",
    hospitalized: "135.0",
    serious: "0",
    discharged: "1899.0",
    deaths: "107",
    effectiveReproductionNumber: "1.03"
  },
  ...
]
```
|項目|内容|
|----|--------|
|id|都道府県コード|
|latest|最新日付|
|prefectureNameJ|都道府県名(和名)|
|prefectureNameE|都道府県名(英語)|
|testedPositive|PCR陽性者数|
|peopleTested|PCR検査数|
|hospitalized|入院患者数|
|serious|重症患者数|
|discharged|退院数|
|deaths|死亡者数|
|effectiveReproductionNumber|実効再生産数|

</details>

---

## Serious

**Endpoint**: [https://covid19-tana-web-api-git-master.tana1024.vercel.app/api/v1/serious](https://covid19-tana-web-api-git-master.tana1024.vercel.app//api/v1/serious)

<details>
<summary><b>Response</b></summary>

```json
[
  {
    date: "2020/02/17",
    serious: "3"
  },
  ...
]
```
|項目|内容|
|----|--------|
|date|対象日付|
|serious|重傷者数|

</details>

---


#  参考サイト
https://github.com/kaz-ogiwara/covid19/  
https://github.com/ryo-ma/covid19-japan-web-api