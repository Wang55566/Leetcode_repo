/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {

  res = [];

  function backtracking(index, subset) {

      if(index === nums.length) {
          res.push(subset.slice())
          return
      }

      subset.push(nums[index])
      backtracking(index + 1, subset)
      subset.pop()
      backtracking(index + 1, subset)

  }

  backtracking(0, [])
  return res
};
