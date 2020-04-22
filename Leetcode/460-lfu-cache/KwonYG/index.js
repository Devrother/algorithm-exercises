class Node {
  constructor(key, value) {
    this.key = key
    this.val = value
    this.next = this.prev = null
    this.freq = 1
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = new Node(null, null)
    this.tail = new Node(null, null)
    this.head.next = this.tail
    this.tail.prev = this.head
  }

  insertHead(node) {
    node.prev = this.head
    node.next = this.head.next
    this.head.next.prev = node
    this.head.next = node
  }

  removeNode(node) {
    let prev = node.prev
    let next = node.next
    prev.next = next
    next.prev = prev
  }

  removeTail() {
    let node = this.tail.prev
    this.removeNode(node)
    return node.key
  }

  isEmpty() {
    return this.head.next.val == null
  }
}

/**
 * @param {number} capacity
 */
const LFUCache = function (capacity) {
  this.capacity = capacity
  this.currentSize = 0
  this.leastFreq = 0
  this.nodes = {} // 순서에 상관없이 노드들이 저장되는 공간
  this.freqs = {} // 참조횟수를 키값으로 가지는 이중 연결 리스트 저장 공간
}

/**
 * @param {number} key
 * @return {number}
 */
LFUCache.prototype.get = function (key) {
  let node = this.nodes[key]
  if (!node) {
    return -1
  }

  this.freqs[node.freq].removeNode(node)

  // 다음에 어떤 항목을 제거할 지 결정한다.
  if (node.freq == this.leastFreq && this.freqs[node.freq].isEmpty()) {
    this.leastFreq++
  }

  node.freq++
  if (this.freqs[node.freq] == null) {
    this.freqs[node.freq] = new DoublyLinkedList()
  }

  this.freqs[node.freq].insertHead(node)

  return node.val
}

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LFUCache.prototype.put = function (key, value) {
  if (this.capacity == 0) {
    return
  }
  let node = this.nodes[key]

  if (!node) {
    this.currentSize++
    if (this.currentSize > this.capacity) {
      let tailKey = this.freqs[this.leastFreq].removeTail()
      delete this.nodes[tailKey]
      this.currentSize--
    }
    let newNode = new Node(key, value)

    if (this.freqs[1] == null) {
      this.freqs[1] = new DoublyLinkedList()
    }
    this.freqs[1].insertHead(newNode)

    this.nodes[key] = newNode
    this.leastFreq = 1
  } else {
    node.val = value
    this.freqs[node.freq].removeNode(node)

    if (node.freq == this.leastFreq && this.freqs[node.freq].isEmpty()) {
      this.leastFreq++
    }

    node.freq++

    if (this.freqs[node.freq] == null) {
      this.freqs[node.freq] = new DoublyLinkedList()
    }

    this.freqs[node.freq].insertHead(node)
  }
}

const cache = new LFUCache(5 /* capacity */)

console.log(cache.put(1, 1)) // freqs 상태: {1: 1}
console.log(cache.put(2, 2)) // freqs 상태: {1: 2 <-> 1}
console.log(cache.put(3, 3)) // freqs 상태: {1: 3 <-> 2 <-> 1}
console.log(cache.put(4, 4)) // freqs 상태: {1: 4 <-> 3 <-> 2 <-> 1}
console.log(cache.put(5, 5)) // freqs 상태: {1:  5 <-> 4 <-> 3 <-> 2 <-> 1}
console.log(cache.get(1)) // 1 반환  freqs 상태: {1:  5 <-> 4 <-> 3 <-> 2,  2: 1}
console.log(cache.get(1)) // 1 반환  freqs 상태: {1:  5 <-> 4 <-> 3 <-> 2,  3: 1}
console.log(cache.get(1)) // 1 반환  freqs 상태: {1:  5 <-> 4 <-> 3 <-> 2,  4: 1}
console.log(cache.put(6, 6)) // freqs 상태: {1:  6 <-> 5 <-> 4 <-> 3,   4: 1}
console.log(cache.get(6)) // 1 반환  freqs 상태: {1:  5 <-> 4 <-> 3 <-> 2,  4: 1  2:6}
