let nums = [1, 5, 6, 7, 1, 7];
var singleNumber = function (nums) {
	return nums.filter(a => nums.indexOf(a) === nums.lastIndexOf(a));
};
