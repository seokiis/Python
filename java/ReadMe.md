# Compareable vs Comparator

모두 객체를 비교할 수 있게 해준다.

## Comparable

- compareTo 메서드는 파라미터가 1개다.
- **"자기 자신과 매개변수 객체를 비교"**
- lang 패키지에 있어 import 필요 X

```java
@Override
public int compareTo(T o){}
```

Comparable은 자기 자신과 매개변수 객체를 비교한다고 했다. 즉, 자기자신은 ClassName으로 생성한 객체 자신이 되고, 매개변수 객체는 ClassName.compareTo(o); 를 통해 들어온 파라미터 o가 비교 할 객체가 되는 것이다.

```java
public class ClassName implements Comparable<Type> {

/*
  ...
  code
  ...
 */

	// 필수 구현 부분
	@Override
	public int compareTo(Type o) {
		/*
		 비교 구현
		 */
	}
}
```

Student 클래스에 Comparable 을 implements 해야한다. 그리고 <> 사이에 들어갈 타입은 무엇일까? Student 객체와 또 다른 Student 객체를 비교하고 싶다면, <> 사이에 들어갈 타입 또한 Student가 되어야하지 않겠는가?

즉, Type 은 Student로 바뀌게 된다.

```java
class Student implements Comparable<Student> {

	int age;			// 나이
	int classNumber;	// 학급

	Student(int age, int classNumber) {
		this.age = age;
		this.classNumber = classNumber;
	}

	@Override
	public int compareTo(Student o) {
		/*
		 * 비교 구현
		 */
	}
}
```

이제 compareTo 메소드를 구현해야 할 것이다. 만약 나이를 기준으로 비교(대소 관계)를 하고자 한다면 어떻게 하면 될까?

자기 자신의 age(나이)와 매개변수로 들어온 o의 age(나이)의 값을 비교하면 된다.

```java
class Student implements Comparable<Student> {

	int age;			// 나이
	int classNumber;	// 학급

	Student(int age, int classNumber) {
		this.age = age;
		this.classNumber = classNumber;
	}

	@Override
	public int compareTo(Student o) {

		// 자기자신의 age가 o의 age보다 크다면 양수
		if(this.age > o.age) {
			return 1;
		}
		// 자기 자신의 age와 o의 age가 같다면 0
		else if(this.age == o.age) {
			return 0;
		}
		// 자기 자신의 age가 o의 age보다 작다면 음수
		else {
			return -1;
		}
	}
}
```

위와같이 두 값의 차를 반환해버리면 번거로운 조건식 없이 한방에 3개의 조건을 만족할 수 있다.

```java
class Student implements Comparable<Student> {

	int age;			// 나이
	int classNumber;	// 학급

	Student(int age, int classNumber) {
		this.age = age;
		this.classNumber = classNumber;
	}

	@Override
	public int compareTo(Student o) {

		/*
		 * 만약 자신의 age가 o의 age보다 크다면 양수가 반환 될 것이고,
		 * 같다면 0을, 작다면 음수를 반환할 것이다.
		 */
		return this.age - o.age;
	}
}
```

## Comparator

- compare 메서드는 파라미터가 2개다.
- **"두 매개변수 객체를 비교"**
- util 패키지에 존재

```java
@Override
public int compare(T o1, T o2){}
```

"두 매개변수 객체를 비교"한다고 했다.

이 말은 자기 자신이 아니라 파라미터(매개 변수)로 들어오는 두 객체를 비교하는 것이다. 여기서 바로 Comparable과 차이가 발생하는 것이다.

```java
import java.util.Comparator;	// import 필요
public class ClassName implements Comparator<Type> {

/*
  ...
  code
  ...
 */

	// 필수 구현 부분
	@Override
	public int compare(Type o1, Type o2) {
		/*
		 비교 구현
		 */
	}
}
```

```java
import java.util.Comparator;	// import 필요
class Student implements Comparator<Student> {

	int age;			// 나이
	int classNumber;	// 학급

	Student(int age, int classNumber) {
		this.age = age;
		this.classNumber = classNumber;
	}

	@Override
	public int compare(Student o1, Student o2) {

		// o1의 학급이 o2의 학급보다 크다면 양수
		if(o1.classNumber > o2.classNumber) {
			return 1;
		}
		// o1의 학급이 o2의 학급과 같다면 0
		else if(o1.classNumber == o2.classNumber) {
			return 0;
		}
		// o1의 학급이 o2의 학급보다 작다면 음수
		else {
			return -1;
		}
	}
}
```

```java
import java.util.Comparator;	// import 필요
class Student implements Comparator<Student> {

	int age;			// 나이
	int classNumber;	// 학급

	Student(int age, int classNumber) {
		this.age = age;
		this.classNumber = classNumber;
	}

	@Override
	public int compare(Student o1, Student o2) {

		/*
		 * 만약 o1의 classNumber가 o2의 classNumber보다 크다면 양수가 반환 될 것이고,
		 * 같다면 0을, 작다면 음수를 반환할 것이다.
		 */
		return o1.classNumber - o2.classNumber;
	}
}
```
