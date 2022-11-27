# 107 北科大碩士資工程式設計

## Problem 4 Code

| Priblem | Answer |
|---|---|
|4-1| bool lessThan()=0;|
|4-2| mValue / _size |
|4-3| *_score |
|4-4| T *score |
|4-5| T mValue |
|4-6| 87 |
|4-7| data set 1:85 <br> data set 2 : 84 |
|4-8| 0 |

本題考抽象介面及繼承概念

### 4-6

```c++
    Data data(8); // 80,82,84,86,88,90,82,94
    data.mean(); // sum(_score) / _size -> 696 / 87 
```

### 4-7、4_8

```c++
    int score[] = {90,80,85,88,86};
    Group g(5,score);
    // data1 90,80,85,88,86
    // data2 80,82,84,86,88

    g.print(); 
    //data1 -> int(sum(data1) / _size) = 429 / 5 = 85
    //data2 -> int(sum(data2) / _size) = 420 / 5 = 84

    g.lessThan(); 
    // 比較大小 return False(0)
```
