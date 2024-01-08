# 파이썬 문법 및 알고리즘 정리
## 🐻‍❄️ 목차
1. [문자열 전처리](#1.-문자열-전처리)   
2. [자료형 Deque](#2.-자료형-Deque)   
3. [문자열 리스트 뒤집기](#3.-문자열-리스트-뒤집기)
4. [숫자 여부 확인 함수](#4.-숫자-여부-확인-함수)
5. [정렬](#5.-정렬)

### 1. 문자열 전처리
> [leetcode 125](https://leetcode.com/problems/valid-palindrome/)
- 영문자, 숫자만 대상으로하고, 대소문자를 구분하지 않음
  1. isalnum() 함수와 리스트 사용   
     💡 **isalnum()**
     : 영문자와 숫자 여부를 판별하는 함수 (영문자 또는 숫자라면 true, 아니라면 false)
      ```
      s = input()
      strs = []
      for char in s:
        if char.isalnum():
          strs.append(char.lower())
      ```
        
    2. 정규식(regex 패턴) 사용   
       💡 **re.sub(패턴, 바꿀 문자열, 문자열, 바꿀 횟수)**   
       - 패턴
          - **[a-z0-9]**: a부터 z까지와 0부터 9까지
          - **^** : 여집합 ex) [^a-z0-9] : a부터 z까지와 0부터 9까지를 제외한 모두
          - **\d** : [0-9]와 동일
          - **\D** : [^0-9]와 동일
          - **\s** : 모든 공백 문자 [ \t\n\r\f\v]와 동일
          - **\S** : 모든 비공백 문자 [ ^\t\n\r\f\v]와 동일
          - **\w** : 모든 영숫자 [a-zA-Z0-9_]와 동일
          - **\W** : 모든 비영숫자 [^a-zA-Z0-9_]와 동일
        
        `import re`
        
        ```jsx
        strs = s.lower()
        strs = re.sub('[^a-z0-9]', '', strs)
        ```

### 2. 자료형 Deque
> [leetcode 125](https://leetcode.com/problems/valid-palindrome/)      

`import collections`   
※ leetcode에는 내장되어있기 때문에 따로 import할 필요없음.   
```
strs = collections.deque()
```

### 3. 문자열 리스트 뒤집기
> [leetcode 344](https://leetcode.com/problems/reverse-string/)   

- 반환 없이 리스트 자체 뒤집기
    1. 투포인터 방식      
        ```
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        ```
        
    2. 파이썬 내장 함수 사용   
        reverse()는 리스트에만 제공됨. 만약 입력값이 문자열이라면 문자열 슬라이싱 `s = s[::-1]`을 사용할 수도 있다.   
        ※ leetcode에서는 공간 복잡도 O(1)로 제한함으로서 변수 할당을 처리하는데 제약이 있음. `s[:] = s[::-1]` 트릭 사용하면 가능함. 이건 플랫폼마다 다르므로 테스트 필요.   
        
        ```
        s.reverse()
        ```

    💡 **파이썬의 swap 원리**   
    다른 언어는 tmp를 통해 swap이 가능한 것과 달리 파이썬에서는 `s[start], s[end] = s[end], s[start]` 이와 같은 코드로 바로 swap이 가능한 이유?   
    : 파이썬에서는 여러 값을 동시에 여러 변수에 할당할 수 있는 튜플 언패킹이라는 기능을 사용한다. 예를 들어 a, b = 1, 2이면 튜플 (1, 2)가 먼저 만들어지고 각각의 값이 변수 a, b에 할당되는데. 이 원리로 swap이 가능한 것이다.   

### 4. 숫자 여부 확인 함수
> [leetcode 937](https://leetcode.com/problems/reorder-data-in-log-files/description/)   

: **isdigit()**   

Q. 문자열 중에 일부가 숫자인지 확인할 때, `log.split()[1].isdigit()` → 숫자라면 True, 아니라면 False

### 5. 정렬
> [leetcode 937](https://leetcode.com/problems/reorder-data-in-log-files/description/)   

단순히 정렬하는 것이 아니라 특정 기준으로 정렬해야 할 때, `문자열.sort(정렬 기준으로 할 것을 반환하는 함수)`   

💡 **람다 표현식 (Lambda Expression)**   
: 식별자 없이 실행 가능한 함수 → 함수 선언 없이도 하나의 식으로 함수를 단순하게 표현할 수 있음.   
→ 람다 표현식은 간단한 함수를 쉽게 표현하는 방법이라고 할 수 있음.   

```
def func(x):
        return x.split()[1], x.split()[0]

s.sort(key=func)
```

이것을 람다표현식을 사용하면 아래와 같이 만들 수 있음.   

```
s.sort(key=lambda x: (x.split()[1], x.split()[0]))
```

하지만 람다 표현식 코드가 길어지고 map이나 filter와 함께 섞어서 사용하는 것은 가독성이 매우 떨어져 좋지 않다. 그때는 함수를 따로 만들어서 사용하자.   
