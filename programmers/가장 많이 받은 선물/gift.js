function solution(friends, gifts) {
  const peopleIndex = {};

  friends.forEach((name, index) => {
    peopleIndex[name] = index;
  });

  const giftMap = Array.from({ length: friends.length }, () =>
    Array.from({ length: friends.length }, () => 0)
  );
  const giftPoint = Array.from({ length: friends.length }, () => 0);

  for (let i = 0; i < gifts.length; i++) {
    const [send, recieve] = gifts[i].split(" ");
    giftMap[peopleIndex[send]][peopleIndex[recieve]] += 1;
    giftPoint[peopleIndex[send]] += 1;
    giftPoint[peopleIndex[recieve]] -= 1;
  }

  const answer = Array.from({ length: friends.length }, () => 0);

  for (let i = 0; i < friends.length; i++) {
    for (let j = 0; j < friends.length; j++) {
      if (giftMap[i][j] > giftMap[j][i]) {
        answer[i] += 1;
      } else if (giftMap[i][j] == giftMap[j][i]) {
        if (giftPoint[i] > giftPoint[j]) {
          answer[i] += 1;
        }
      }
    }
  }
  return Math.max(...answer);
}

console.log(
  solution(
    ["muzi", "ryan", "frodo", "neo"],
    [
      "muzi frodo",
      "muzi frodo",
      "ryan muzi",
      "ryan muzi",
      "ryan muzi",
      "frodo muzi",
      "frodo ryan",
      "neo muzi",
    ]
  )
);
console.log(
  solution(
    ["joy", "brad", "alessandro", "conan", "david"],
    [
      "alessandro brad",
      "alessandro joy",
      "alessandro conan",
      "david alessandro",
      "alessandro david",
    ]
  )
);

console.log(
  solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"])
);
