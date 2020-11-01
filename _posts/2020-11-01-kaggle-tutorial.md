---
title: Intro to Machine Learning
category: review
---

캐글 사이트에 기본 튜토리얼로 있는 내용을 읽어보았다.
https://www.kaggle.com/learn/intro-to-machine-learning

# Decision Tree
Data science 의 용도로 **basic** 한  **model** 이며 , 새로운 데이터가 들어왔을 때 기존 데이터를 통해 **decision tree** 를 구성하여 예측한다.
- 내가 1000원이 있다면 과자를 살 수 있다. 그렇지 않다면 과자를 살 수 없다.

가장 simple 한 상황인데 이상한 점을 느낄 수 있다.
1000원 없는데 만약 1100원인 경우 혹은 900원이 있는 경우와 같이 조금 더 깊게 생각해볼 수 있다.
그래서 이 상황들까지 하위 레벨로 내려가며 상황들에 대한 값을 정의해준다면 트리가 깊어지게 된다.
이를 기존 tree 를 **split** 하여 **deeper** tree 를 만들었다고 볼 수 있게된다.

그리고 모든 조건을 통해 가장 마지막 값에 도달한 경우 이를 leaf 에 도달했다고 할 수 있고 해당 값으로 **예측**되었다고도 할 수 있다.

# Basic Data Exploration
pandas 는 data 를 **manipulate**, **explore** 하기 위해 사용되는 data science 용 tool 이다.
- [simple example](https://www.kaggle.com/kshcode/notebook653880a6c6)

## Exercise
- 완료, 빈칸 채우기 느낌임

# Your First Machine Learning Model
예측할 값을 **prediction value**, 예측을 위한 컬럼들을 **features** 라고 한다.
데이터가 잘 입력, 출력되는지 시각적으로 검증하는 것이 data science 에서는 중요한 작업이다.

## Building Your Model
- Define: 사용할 모델 정의, 파라매터 사용 어떻게 할 것인가 정의
- Fit: 제공된 데이터를 통해 capture patterns 해야된다.
- Predict: 말 그대로 예측
- Evaluate: 사용한 모델로 predicgt 한 값이 얼마나 실제에 근사한지 확인

일반적으로 위 4단계를 순서대로 진행한다.

나머지는 시간날 때 이어서..
