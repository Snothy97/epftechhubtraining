function isPalindrome(number) {
    const stringified = String(number);
    const reversed = stringified.split('').reverse().join('');
    return stringified === reversed;
  }
  
  function findLargestPalindrome() {
    let largestPalindrome = 0;
    for (let i = 999; i >= 100; i--) {
      for (let j = 999; j >= 100; j--) {
        const product = i * j;
        if (isPalindrome(product) && product > largestPalindrome) {
          largestPalindrome = product;
        }
      }
    }
    return largestPalindrome;
  }
  
  const largestPalindrome = findLargestPalindrome();
  console.log(largestPalindrome);
  