# Algorithm

# Greedy

[Sorting](https://www.notion.so/Sorting-0e6d08e6771b46d08d8c3e29f99b1673)

[Dynamic Programming](https://www.notion.so/Dynamic-Programming-acf50f9c18df4fa6b54c6f78591f1de7)

[Search](https://www.notion.so/Search-f26e1396400e41fe910cb3f4bb8d5e69)

[백트래킹](https://www.notion.so/a4f68984890342a3b7044315623a5c99)

[Pattern Matching](https://www.notion.so/Pattern-Matching-866b3308da7e4c1a867083d6c9da68a1)

[Divide & Conquer](https://www.notion.so/Divide-Conquer-7eb99b29b7aa46a9994c18c8abb70472)

[Dijkstra](https://www.notion.so/Dijkstra-ea09117f5a964649b1132f35eee64c4c)

### 정의

- 문제 해결 방법을 추상화하여 단계적 절차를 논리적으로 기술한 명세서

### 조건

- 입력 : 필요한 자료가 외부에서 입력으로 제공됨
- 출력 : 하나 이상의 결과물이 출력되어야 함
- 명확성 : 수행 작업의 내용과 순서를 나타내는 알고리즘의 명령어들은 명확히 정의되어야 함
- 유한성 : 실행 후 반드시 종료되어야 함
- 효과성 : 알고리즘의 모든 명령어들은 기본적이며 실행 가능해야 함

### 좋은 알고리즘?

- 정확성 : 유한한 시간 내에 정확한 결과 출력
- 단순/명확성 : 얼마나 이해하기 쉽고 명확한가
- 수행/작업량 : 연산이 얼마나 적은가
- 메모리 사용량 : 가능한 적은 메모리 사용
- 최적성 : 최적화된 성능을 가져야 함

### 알고리즘의 표현방법

- 자연어에 의한 서술적 표현
- 순서도 (Flow Chart)를 이용한 도식화 표현
- Pseudo Code
- 코드 (프로그래밍 언어)

------

## Time Complexity

: 알고리즘의 작엽량. 연산 횟수, 실행되는 명령문의 수가 어느정도인가

### Big O 표기법

- 알고리즘과 데이터의 구현 형태나 크기에 따라 계산횟수의 대략적인 표기
- 시간 복잡도 함수 중 가장 큰 영향력을 주는 n만을 계수를 생략 ex. O(2n+1) = O(n)

![bigo](https://user-images.githubusercontent.com/82459236/157072887-b2e89ef8-c4f6-4868-ad2f-7b768a5a3f5e.png)

# Data Structure

- 자료를 효율적으로 표현, 저장하고 처리할 수 있도록 정리하는 것

![datastructure](https://user-images.githubusercontent.com/82459236/157072937-9cac3420-c7c6-4d8f-a1f1-0755ee08f074.png)

- 단순 구조

  - 정수, 실수, 문자, 문자열 등

- 선형 구조

  - 자료 관계가 1:1 / 리스트, 연결리스트, 스택, 큐, 덱
  - 구현할 자료들을 논리적인 순서대로 메모리에 차례로 저장하는 구현 방식
  - 논리 순서와 물리적 순서가 일치 (연결리스트 제외)

  [Array/List](https://www.notion.so/Array-List-0fe320f97c0e4451bf729acdc241fac5)

  [Linked List](https://www.notion.so/Linked-List-2d5a61ce5d614ebd98f4152a6dd49305)

  - List vs Linked List

  | 구분                                         | List                                                         | Linked List |
  | -------------------------------------------- | ------------------------------------------------------------ | ----------- |
  | 메모리 저장 방식                             | 메모리의 저장 시작 위치부터 공백 없이 순서대로 저장          |             |
  | 논리적 순서와 물리적 순서가 일치             | 메모리에 저장된 물리적 위치가 논리적 순서와 관계 없음        |             |
  | 연결에 의해 논리적 순서를 구현               |                                                              |             |
  | 연산 특징                                    | 삽입, 삭제 연산 후에도 자료의 연속성이 유지됨                |             |
  | 변경된 논리적 순서에 따라 물리적 위치 재배열 | 삽입, 삭제 연산 후에도 연결 링크 정보만 변경되며 물리적 위치가 변경되지 않음 |             |
  | 구현                                         | 배열                                                         | 포인터      |

  [Stack](https://www.notion.so/Stack-9eb2de845be940b1a62cfdb134715d6a)

  [Queue](https://www.notion.so/Queue-b920016814a1430485f7dd26a390c44f)

  - Deque : double-ended queue
    - 큐 + 뒤집힌 큐 형태로, 자료의 양 끝에서 삽입/삭제가 모두 가능한 자료구조

- 비선형 구조

  - 자료 관계가 1:N 또는 M:N / 트리, 그래프

    [Tree](https://www.notion.so/Tree-a6c38c46caae4bb8bf9e9e21541a7235)

    [Graph](https://www.notion.so/Graph-2003752b79154c91acc777d9adad6d9b)

- 파일 구조

  - 서로 관련있는 필드로 구성된 레코드의 집합인 파일 구조
  - 순차 파일, 색인 파일, 직접 파일

[Heap](https://www.notion.so/Heap-2dc27f85a71a4dc38e828402c4af9b30)

[Hash Table](https://www.notion.so/Hash-Table-cb00d1b37dbb45f582bf51a2c0a4fabd)
