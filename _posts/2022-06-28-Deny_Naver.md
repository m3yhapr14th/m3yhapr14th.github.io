---
layout: post
title: "북한이 네이버를 차단하게 하는 법"
subtitle: 회사에서 북한이 네이버를 못 보게하는 기발한 방법
gh-repo: m3yhapr14th/basic_edu
gh-badge: [star, fork, follow]
tags: [Security]
comments: true
---

![mc_pzs_kr](/assets/img/mc_pzs_kr.jpg)

오늘 퇴근하려고 하니 사용자 PC에서 네이버가 접속되지 않는다는 장애 건을 접수받았다.
인터넷이 되는 PC 2대에서 확인해보니 웹격리 솔루션을 타고 나가는 PC는 잘 되는데 내부에서 외부로 직접 나가는 PC는 안되는 것이다.
<br>
바로 방화벽 로그를 뒤져보니 naver.com의 Lookup된 IP로 차단되는 게 보이는 것이 아닌가.
해당 방화벽 정책에 보니 네이버 IP나 DNS 객체는 없었다.
<br>
하필 Juniper 방화벽이라 객체 보기도 힘든데 어찌됐든 침해지표에 해당하는 URL을 차단한 정책이라 dns 정보를 전부 확인해야했다.
다행히 정책에서 Lookup된 정보를 불러오는 명령어가 있었고 금방 확인할 수 있었다.
<br>
```
show security policies policies-name [정책명] detail
```
<br>
특정 객체에서 네이버 IP를 확인했고 dns-name을 보니 <font color=red>mc.pzs.kr</font> 이었다.
그 url은 06/15에 업체를 통해 제공받았던 <font color=skyblue>긴급 북한 발 침해지표 리스트</font> 내에 있었던 URL 정보였다.
<br>
영악하게도 북한 발 악성 URL이라고 퍼뜨려놓고 2주 뒤 URL의 DNS를 CNAME으로 naver.com을 설정해놓은 것이다.
침해지표를 받아 차단한 기업들은 대부분 비슷한 대응을 했을 것이다.
<br>
웃겨 정말..

