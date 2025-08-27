class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        let n = nums.count
        if n <= 1 { return }
        let k = k % n
        if k == 0 { return }

        reverse(&nums, 0, n - 1)
        reverse(&nums, 0, k - 1)
        reverse(&nums, k, n - 1)
    }

    private func reverse(_ nums: inout [Int], _ left: Int, _ right: Int) {
        var l = left, r = right
        while l < r {
            nums.swapAt(l, r)
            l += 1
            r -= 1
        }
    }
}
