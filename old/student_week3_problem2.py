import array


class Queue:
    def __init__(self):
        # 1001개의 short 정수를 저장할 고정 크기의 배열을 생성
        self.data = array.array('h', [0] * 1001)
        self.front = 0  # 큐의 맨 앞 인덱스
        self.rear = 0  # 큐의 맨 뒤 인덱스
        self.capacity = 1001  # 배열의 총 용량

    def enqueue(self, item):
        # 큐에 item을 추가하는 메소드
        # 큐가 가득 찼는지 확인: 다음 rear 인덱스가 front와 같으면 가득 찬 상태
        next_rear = (self.rear + 1) % self.capacity
        if next_rear == self.front:
            raise IndexError("Queue is full")
        self.data[self.rear] = item  # 현재 rear 위치에 item 저장
        self.rear = next_rear  # rear 인덱스를 업데이트 (원형 큐이므로 모듈러 연산 사용)

    def dequeue(self):
        # 큐에서 맨 앞의 원소를 제거하고 반환하는 메소드
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.data[self.front]  # front 위치의 데이터를 가져옴
        self.front = (self.front + 1) % self.capacity  # front 인덱스를 업데이트
        return item

    def is_empty(self):
        # 큐가 비었는지 확인: front와 rear가 같으면 큐는 비어 있음
        return self.front == self.rear


class CardGame:
    def __init__(self):
        # CardGame 클래스는 Queue를 사용하여 카드 게임을 시뮬레이션
        self.cards = Queue()

    def lastCard(self, n):
        """
        lastCard(n): 1부터 n까지의 카드를 순서대로 큐에 넣고,
        다음 두 가지 연산을 반복하여 마지막으로 남는 카드 번호를 반환한다.
          1. 맨 위의 카드를 버린다. (dequeue)
          2. 그 다음 카드(맨 위의 카드)를 맨 뒤로 옮긴다. (dequeue 후 enqueue)
        """
        # 1부터 n까지의 카드를 큐에 삽입
        for i in range(1, n + 1):
            self.cards.enqueue(i)
        ret = None
        # 큐에 카드가 하나 남을 때까지 다음 연산 수행
        while not self.cards.is_empty():
            ret = self.cards.dequeue()  # 맨 위의 카드를 버림(저장해두지만 최종 결과로 사용)
            if self.cards.is_empty():
                # 카드가 하나 남았다면 반복 종료
                break
            # 다음 맨 위의 카드를 꺼내서 다시 큐의 맨 뒤로 보냄
            self.cards.enqueue(self.cards.dequeue())
        return ret


def main():
    cardGame = CardGame()
    # 카드의 개수에 따라 마지막에 남는 카드 번호를 출력
    print(cardGame.lastCard(1))  # 1장일 경우, 마지막 카드: 1
    print(cardGame.lastCard(4))  # 4장일 경우, 마지막 카드: 4
    print(cardGame.lastCard(7))  # 7장일 경우, 마지막 카드: 6 (예시)
    print(cardGame.lastCard(1000))  # 1000장일 경우, 마지막 카드 번호 출력


if __name__ == "__main__":
    main()
