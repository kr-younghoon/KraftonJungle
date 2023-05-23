# Weekly I Learned | Webproxy-lab

# 10.5. RIO Package 📦

<aside>
🔥 이번 주차를 알아가기 전에 네트워크 소켓 통신에서 사용하게 될 CS.APP 10.5장의 개념 `RIO Package`를 알아보고 Web-proxy에 대해 공부해 봅시다!

</aside>

RIO = Robust I/O 입니다. Robust는 무엇입니까 ? → I/O 장치의 특성 때문인데, 입출력 장치를 견고하게 만들어 준다는 의미를 가지고 있습니다.

RIO는 2가지 형태를 띠고 있다. (표 참조)

---

1. 2진 데이터로 이루어진 `Unbuffered Input/Ouput`(*책에서는 버퍼 없는 입력 및 출력 함수라고 표현한다.)

→ 아래에선 `rio_readn`, `rio_writen` 함수로 이를 처리 할 것이다.

1. 2진 데이터와 텍스트로 이루어진 `Buffered Input`(*버퍼를 사용하는 입력함수)

→ 아래에선 `rio_readlineb`, `rio_readnb` 함수로 설명할 것이다. *특히 2번 buffered는 그 전(unix, standard)에서 하지 못하는 스레드 관리를 해주니 자세히 보도록 하자.

## 1. Unbuffered RIO Input and Ouput

---

### 함수 정의

---

```c
#include "csapp.h"
ssize_t rio_readn(int fd, void *usrbuf, size_t n);
ssize_t rio_writen(int fd, void *usrbuf, size_t n);
Return: # of bytes transferred if OK,
0 on EOF (rio_readn only), -1 on error
```

### 설명

---

- 우선 사용하기 위해 “csapp.h”를 불러온다.
- 함수는 읽기(readn), 쓰기(writen) 2가지가 있다.
- rio_readn은 eof 파일을 만나게 되면 short count를 리턴 하지만, rio_writen은 short count를 리턴하진 않는다.
- 추가로 interleaved(중간 간섭)을 허용한다.

<aside>
👀 **→ size_t와 ssize_t의 차이는 무엇인가?**
read 함수는 size_t 입력 인자를 가지며, ssize_t를 리턴 값으로 가지는 것을 눈치챘을지 모른다. 그러면, 이 두가지 타입의 차이는 무엇일까? x86-64에서 size_t는 unsigned long으로 정의되고, ssize_t(signed size)는 long으로 정의된다. read 함수는 비부호형 크기 대신에 부호형 크기를 리턴하는데, 그 이유는 에러 발생 시에 -1 을 리턴해야 하기 때문이다. 흥미로운 것은 한 개의 -1을 리턴할 수 있다는 것이 read의 최대 크기를 4GB 에서 2GB 로 2배 줄여준다는 점이다.

</aside>

## 2. Buffered Input

---

`Buffered I/O`는 RIO에서 버퍼를 관리한다는 의미를 지닌다.

보통 프로그램에서는 1개의 글자를 읽는데 1번의 `시간(cycle)`이 걸린다.

예를 들어 hello를 출력하려면, ‘h’, ‘e’, ‘l’, ‘l’, ‘o’를 각각 따로 출력을 해줘야 한다는 의미로 매우 비효율적이다. 이에 대한 해답은 버퍼를 사용하는 읽기 방식이 되겠는데 이게 `Buffered read`이다.

![Untitled](Weekly%20I%20Learned%20Webproxy-lab%2098a597a364d044cca39dba6af1716c20/Untitled.png)

위 그림은 버퍼를 시각화한 그림인데, 간단합니다요

초록색은 이미 읽은 부분, 빨간색은 아직 읽지 않은 부분을 뜻하고 `rio_buf`는 시작된 지점, `rio_bufptr`은 현재 읽는 부분을 나타내는 포인터, `rio_cnt`는 읽을 부분의 수를 나타낸다.

### 함수 정의

---

```c
#include "csapp.h"
void rio_readinitb(rio_t *rp, int fd);
ssize_t rio_readlineb(rio_t *rp, void *usrbuf, 
	size_t maxlen);
ssize_t rio_readnb(rio_t *rp, void *usrbuf, size_t n);
Return: num. bytes read if OK,
0 on EOF, -1 on error
```

### 설명

---

- rio_readinitb : 초기화 함수이다.
- rio_readlineb : 한 줄 단위로 입력을 받는다. 이 때 파라미터로 입력의 최대 바이트 크기를 넣어주어야 한다.
- rio_readnb : 파일 fd에서 n 바이트 크기를 읽어온다.

위 코드가 종료되는 조건은 파라미터로 입력된 maxlen만큼 읽었을 때, 읽는 도중 EOF가 발생한 경우 그리고 한 줄 입력 같은 경우는 newline(개행) 문자를 만난 경우가 되겠다.

# 11
