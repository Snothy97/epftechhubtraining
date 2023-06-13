function isPalindrome(num) {
  return num.toString() === num.toString().split("").reverse().join("");
}

function largestPalindromeFromProductOfTwo3DigitNumbers() {
  var largestPalindrome = 0;

  for (var i = 100; i < 1000; i++) {
    for (var j = 100; j < 1000; j++) {
      var product = i * j;

      if (isPalindrome(product) && product > largestPalindrome) {
        largestPalindrome = product;
      }
    }
  }

  return largestPalindrome;
}

console.log(largestPalindromeFromProductOfTwo3DigitNumbers()); //printing the largest palindrome
