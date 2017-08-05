# Game A Week
**1주 1겜** 만들기 프로젝트

## 제작자 한마디

**생각하면서 코딩을 합시다... 이번에 이렇게 못했으니 다음엔 안그러겠지..?**



## ClickingMoney
![play](https://user-images.githubusercontent.com/15938440/28994323-38bfd26c-7a06-11e7-90e3-b58c2d1f65be.png)

### 게임 소개
항목의 레벨업을 통해 자원을 불려나가는 클리커 게임 입니다.

### 주요 구현 기능

#### 과금모드/비과금모드
![select](https://user-images.githubusercontent.com/15938440/28994324-38c0188a-7a06-11e7-9eba-f1f30d13eb4f.png)
![select2](https://user-images.githubusercontent.com/15938440/28994321-38beb468-7a06-11e7-9446-5330f9e0b80b.png)

첫 시작시 과금모드만 플레이 가능하고, 과금모드 엔딩 후에는 무과금 모드 플레이가 가능합니다.

#### 화폐와 업그레이드
![money](https://user-images.githubusercontent.com/15938440/28994322-38bfa3be-7a06-11e7-8c31-29753941445e.png)

인게임 화폐로 골드, 인게임내 현금화폐로서 보석을 만들었습니다  
보석은 업그레이드 슬롯 언락, 캐릭터 교체등에 사용됩니다.

#### 저장 기능
![save](https://user-images.githubusercontent.com/15938440/28994319-38b9e35c-7a06-11e7-9f58-c8fe589d41dd.png)

골드, 크리스탈 업그레이드 레벨, 업그레이드 슬롯 언락 유무, 캐릭터 교체 여부 등을 저장합니다.

### 아쉬운 점

###### 깔끔하지 않은 코드

기능의 함수화의 신경쓰다보니 코드의 가독성이 미친듯이 떨어지게 되었습니다.

###### 보안

저장된 txt를 불러올때 eval을 사용합니다 injection등을 통해 공격이 가능합니다  
또한 암호화가 되어있지 않아 얼마든지 수치의 조작이 가능합니다


### 개발 후 깨달은 점

###### 아트작업
![gold](https://user-images.githubusercontent.com/15938440/28994332-5d3ed9b2-7a06-11e7-8f0d-1b0021b5b24b.png)
![diamond](https://user-images.githubusercontent.com/15938440/28994333-5d420e2a-7a06-11e7-917b-55a9c7dd2d75.png)

아트작업의 보람은 최고입니다.  
다만 캐릭터등의 스스로 하기 힘든것은 오픈소스를 사용하는것이 좋습니다

###### 초기 설계의 중요성

이후 구현에 대하여 생각하지 않고 코딩을 하면 후에 걷잡을 수 없는 후폭풍을 불러옵니다

## 라이센스
None

## 제작
* [NotonAlcyone](notonalcyone@gmail.com):    디자인 프로그래밍 아트   
* [쥬얼 세이버](http://www.jewel-s.jp/): 아트 리소스
