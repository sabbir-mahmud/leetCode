// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    var ptr = new ListNode(0);
    var s = ptr;
    var c = 0;

    while (l1 || l2 || c) {
        if (l1) {
            c += l1.val;
            l1 = l1.next;
        }

        if (l2) {
            c += l2.val;
            l2 = l2.next;
        }

        // Set the next node in the result linked list
        ptr.next = new ListNode(c % 10);
        ptr = ptr.next;
        c = Math.floor(c / 10);
    }

    return s.next;
};
