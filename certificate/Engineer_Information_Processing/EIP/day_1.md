---
layout: page
title: 정보처리기사 실기 모의고사 1일차
subtitle: 2022년 2회차 정보처리기사 실기 준비
---

## 문제 풀이

#### 서비스 지향 아키텍처
- 분할된 조각들을 Loosely-Coupled하게 연결하여 하나의 Application을 완성시키는 아키텍처

### 무선 통신 기술

#### 피고넷(PICONET)
- 좁은 환경에서 블루투스 또는 UWB 통신 기술을 이용하여 하나의 통신망을 구성

#### 지그비(ZIGBEE)
- 홈 오토메이션, 데이터 네트워크

#### 정적 테스트

|종류|설명|
|---|:---|
|동료검토|2~3명이 진행하는 리뷰|
|인스펙션|제작자 외 다른 전문가 또는 팀이 오류를 찾아내는 기법|
|워크스루|짧은 시간 동안 회의를 거쳐 오류를 검출|

### DB
#### 특정 단어 출력
```
SELECT * FROM 테이블 LIKE '_단어';
symetric 앞에 1글자의 알파벳이 있는 단어 출력
- asymetric
- Rsymetric
```

### C++
#### switch ~ case
- break가 없을 경우 탈출하지 않고 계속 실행됨

#### JSON
- 속성 - 값, 키 - 값 쌍 등 인간이 읽을 수 있는 개방형 표준 포맷

#### 요구사항 명세 기법

|기법|설명|
|---|---|
|비정형 명세 기법|사용자, 자연어를 기반으로 서술|
|정형 명세 기법|수학적인 원리와 표기법|

#### 병형 제어 미보장 시 문제점
- 갱신 손실
- 현황 파악 오류
- 모순성
- 연쇄 복귀

### 데이터베이스 정규화 단계
#### 정규화

|단계|조건|
|---|---|
|1단계(NF)|원잣값으로 구성|
|2단계|부분 함수 종속 제거|
|3단계|이행 함수 종속 제거|
|보이스-코드 정규형|결정자이면서 후보키가 아닌 것 제거|
|4단계|다치 종속성 제거|
|5단계|조인 종속성 제거|