# 107 北科大碩士資工程式設計

## Problem 3 Code

Infix to Postfix 中序轉後序

| Problem  | Answer  |
|---|---|
| 3-1  | top |
| 3-2  | ++  |
| 3-3  | --  |
| 3-4  | isEmpty  |
| 3-5  | indexp  |
| 3-6  | &&  |
| 3-7  | >=  |
| 3-8  | elem  |
| 3-9  | !shouldPopOp(elem,c)  |
| 3-10  | c  |

### 預算子權重表

| OP  | Priority  |
|---|---|
| ^ | 3 |
| * | 2 |
| / | 2 |
| + | 1 |
| - | 1 |

原則：優先權較高、相同的先執行(OutPut)

## Stack Step

"a+b*c-d/e^f"

| Token  | Stack  | Top | Output
|---|---| --- | --- |
| a |  | -1 | a |
| + | + | 0 | a |
| b | + | 0 | ab |
| * | + *| 1 | ab |
| c | + * | 1 | abc |
| - | -  | 0 | abc*+ |
| d | -  | 0 | abc*+d |
| / | - /  | 1 | abc*+d |
| e | - /  | 1 | abc*+de |
| ^ | - / ^  | 2 | abc*+d |
| f | - / ^  | 2 | abc*+df |
|  | | -1 | abc*+d^/- |

"a*b-c/d^e*f+g*h"

| Token  | Stack  | Top | Output
|---|---| --- | --- |
| a |  | -1 | a |
| * | * | 0 | a |
| b | * | 0 | ab |
| - | - | 0 | ab* |
| c | - | 0 | ab*c |
| / | - / | 1 | ab*c |
| d | - / | 1 | ab*cd |
| ^ | - / ^ | 2 | ab*cd |
| e | - / ^ | 2 | ab*cde |
| * | - *  | 1 | ab*cde^/ |
| f | - *  | 1 | ab*cde^/f |
| + | + | 0 | ab*cde^/f*- |
| g | + | 0 | ab*cde^/f*-g |
| * | + * | 1 | ab*cde^/f*-g |
| h | + * | 2 | ab*cde^/f*-gh |
|  |  | -1 | ab*cde^/f*-gh*+ |
