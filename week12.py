import seaborn as sns
import matplotlib.pyplot as plt

# 1. titanic 데이터셋으로 복습
titanic = sns.load_dataset('titanic')

# 기본 데이터셋
# print(titanic.head())
# print(titanic.describe())
# print(titanic.info())

# 데이터 파악하기
# print(titanic['who'])
# print(titanic['who'].value_counts())
# print(titanic[['deck', 'embark_town']]) # deck(방 번호)
# print(titanic[['alive', 'survived', 'alone']])

# 데이터 날리기
# 기계형 학습의 경우 수치형 데이터를 남겨줘야 학습하기 좋다.
# 다만 embarked, embark_town처럼 글자라면 이걸 수치로 바꿔주는게 좋다. (다만 알아보기는 해야해서 embark_town을 남긴다.)
# print(titanic[['alive', 'survived', 'pclass', 'class', 'embark_town']])
titanic01 = titanic.drop(columns=['embarked', 'alive', 'class', 'deck'])
# print(titanic01.info())



# 2. 70%이상에 육박하는 deck의 결측치 문제 해결하기
# pclass와 deck의 강한 상관관계가 존재한다.
#   - A~D deck는 1~2등급 / E~F deck는 3등급
# print(titanic01['pclass'].value_counts())
# print(titanic01[titanic01['pclass'] == 1])

# pclass별 survived 평균값
# survival_rate_pclass = titanic01.groupby('pclass')['survived'].mean()
# print(survival_rate_pclass)

# # sex별 survived 평균값
# survival_rate_sex = titanic01.groupby('sex')['survived'].mean()
# print(survival_rate_sex)

# who별 survived 평균값
# survival_rate_who = titanic01.groupby('who')['survived'].mean()
# print(survival_rate_who)



# 3. 결측치 처리하기
# age, embark_town << age가 117개라 날리기 애매해서 embark_town을 날리기
titanic01 = titanic01.dropna(subset=['embark_town'])
# print(titanic01.info())

# age 채울 사전 준비
# print(titanic01['age'].mean())
# print(titanic01['age'].median()) # 보통 이걸 많이 쓴다고
# print(titanic01['age'].mode()) # 최빈값은 여러번 나온 값을 뜻한다.

# age 채우기
titanic01['age'] = titanic01['age'].fillna(titanic01['age'].median())
# print(titanic01.info())



# 4. 그래프 띄우기
# sns.barplot(data=titanic01, x='pclass', y='survived')
sns.barplot(data=titanic01, x='who', y='survived')
plt.show()