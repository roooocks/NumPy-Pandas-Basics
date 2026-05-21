import pandas as pd
# 파이썬 기본 그래픽을 사용한다고...
import seaborn as sns
# import matplotlib.pyplot as plt


# 1. 10주차 일부 복습
# mpg = sns.load_dataset('mpg')
# print(mpg['model_year'].value_counts().sort_values(ascending=False))
# print(mpg.sort_values('model_year', ascending=False)) # mpg로 하면 연비가 높은 차량부터 나온다.

# mpg = sns.load_dataset('mpg')
# mpg = mpg.drop(columns=['origin', 'name', 'model_year'])
# print(mpg[mpg['horsepower'].isnull()], '\n') # mpg['horsepower'].isnull()만 하면 정확히 horsepower에 대한 값만 나온다. index만 존재하는 채로 말이다.



# 2. exercise 데이터 시트에서 필요한 정보들 취합
# ex = sns.load_dataset('exercise')

# print(ex.head(10))
# print(ex.info())

# print(ex['kind'].value_counts()) # 3가지 30개 (reset, walking, running)
# print(ex['time'].value_counts()) # 3가지 30개 (10min, 50min, 30min)
# print(ex['diet'].value_counts()) # 2가지 45개 (no fat, law fat)

# 아래 자료를 no fat으로 보면 맨 아래 9개의 자료는 시간 대비 심박수의 변동폭이 크다.
# 반대로 law fat은 반대다.
# print(len(ex[ex['diet'] == 'low fat'])) # 그냥 쓰면 조건에 맞는 테이블 내용이 나온다.
# print(ex[ex['diet'] == 'low fat'])



# 3. exercise 데이터 시트 정제 후 시각화 (그래프)
# ex = sns.load_dataset('exercise')
# running_df = ex[ex['kind'] == 'running'] # reset, walking, running
# print(running_df)

# GUI 그래프
# 그래프를 보면 알겠지만 30분 때는 심박수가 겹치지 않고 무지방은 심박수가 130 미만이 없다.
# 또한 15분때는 저지방 참가자들의 심박수가 엄청나게 폭이 크고 반대로 30분 때는 안정화가 된 상태다.
# sns.catplot(data=running_df, x='time', y='pulse', hue='diet', kind='point') # 식단별로 시간당 심박수를 point 형태로 본다.
# plt.show()



# 4. exercise 데이터 시트 정제
ex = sns.load_dataset('exercise')

# 조건은 "저지방 & 30분 & 러닝"으로 "심박수 평균"
# 3번의 그래프 시각화와 같이 보면 좋다. 실제로도 110 조금 위를 가리킨다.
ex = ex[
    (ex['diet'] == 'low fat') &
    (ex['time'] == '30 min') &
    (ex['kind'] == 'running')
]
print(ex)

mean_pulse = ex['pulse'].mean()
print(mean_pulse)