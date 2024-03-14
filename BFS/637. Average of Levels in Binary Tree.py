/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var averageOfLevels = function(root) {
        if (!root) return [];

        const queue = [root];
        const res = [];

        while (queue.length > 0) {
            let levelSum = 0;
            const levelLength = queue.length;

            for (let i = 0; i < levelLength; i++) {
                const node = queue.shift();
                levelSum += node.val;

                if (node.left) {
                    queue.push(node.left);
                }
                if (node.right) {
                    queue.push(node.right);
                }
            }

            res.push(levelSum / levelLength);
        }

        return res;

};
