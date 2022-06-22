---
layout: page
title: 2022 정보처리기사 실기 공부
subtitle: 모의고사 정리 2일차
---

## 용어 정리

## 코딩 및 DB 문제
```
i = 0
sum = 0

while i < 10:
    i = i + 1
    if i % 3 == 0:
        sum -= 1
    elif i % 3 == 1:
        sum += 1
    else:
        sum *= 2

print(sum)
```
#### 답지 풀이
|i|i%3|sum|
|---|---|---|
|0||0|
|1|1|1|
|2|2|2|
|3||
|4||
|5||
|6||
|7||
|8||
|9||
||129(119+10)|

위 내용대로는 이해가 되지 않아 직접 코딩하면서 각 단계 별 print를 추가, 로직을 이해하였다.
```
i = 0
sum = 0

while i < 10:
    print("현재 i={0}, sum={1}".format(i,sum))
    i = i + 1
    print("다음은 i={0}, sum={1}".format(i,sum))
    if i % 3 == 0:
        sum -= 1
    elif i % 3 == 1:
        sum += 1
    else:
        sum *= 2
    print("결과 i={0}, sum={1}".format(i,sum))

print(sum)
```
i = i + 1에 대해 이해하는 부분이 어려워 i와 i+1을 분리
|i|i+1|i%3|sum|
|---|---|---|---|
|0|||0|
|0|1|1|1|
|1|2|2|2|
