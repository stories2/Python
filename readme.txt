2016 05 29
어제 개발한 소스를 토대로 쓰레드와 클래스를 사용해 소스를 구조화 시켰으며 또한 동시 접속이 가능하도록 만듦
MainService 에서 클라이언트의 접근 요청을 받아들임
ClientService 에서 각각의 클라이언트와 상호작용을 함
TxService 에서 서버-> 클라이언트로 정보를 보냄
RxService 에서 클라이언트-> 서버로 정보를 받음
Queue 에서 버퍼 데이터를 저장함

문제점
html 소스를 전부 보냈음에 불구하고 브라우저에서는 로딩중으로 표시되는 오류

2016 05 28
GET / HTTP/1.1\r\n
으로 시작하는 http request header 데이터가 들어오면 response 하면서 약간의 html 소스를 반환함
본 프로그램은 python 3.5 로 작성되었으며 socket 을 사용함