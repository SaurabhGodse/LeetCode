using System.Linq;

namespace Leetcode_Daily_Questions
{
    public class CountingSort
    {
        public static void Main(string[] args)
        {
            CountingSort countingSort = new CountingSort();
            int[] nums = { 5, 2, 3, 1 };
            countingSort.SortArray(nums);
        }

        /*
         * Problem 912 Sort an array can also be solved using counting sort. This is giving best time complexity for that problem.
         */
        public int[] SortArray(int[] nums)
        {
            int min = nums.Min();
            int max = nums.Max();
            int[] freq = new int[max - min + 1];
            for (int i = 0; i < nums.Length; i++)
            {
                freq[nums[i] - min]++;
            }
            int j = 0;
            for (int i = 0; i < freq.Length; i++)
            {
                if (freq[i] > 0)
                {
                    while (freq[i] > 0)
                    {
                        freq[i]--;
                        nums[j++] = i + min;
                    }
                }
                if (j >= nums.Length)
                {
                    break;
                }
            }
            return nums;
        }
    }
}
