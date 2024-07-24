using System.Collections.Generic;
using System;

namespace Leetcode_Daily_Questions
{
    public class SortJumbledNumbers
    {
        static void Main(string[] args)
        {
            int[] mapping = { 8, 9, 4, 0, 2, 1, 3, 5, 7, 6 };
            int[] nums = { 991, 338, 38 };
            SortJumbledNumbers sort = new SortJumbledNumbers();
            Console.WriteLine(sort.SortJumbled(mapping, nums));
        }

        public int[] SortJumbled(int[] mapping, int[] nums)
        {
            Dictionary<int, int> mappedValues = new Dictionary<int, int>();
            Dictionary<int, int> indexValues = new Dictionary<int, int>();
            for (int i = 0; i < nums.Length; i++)
            {
                mappedValues[nums[i]] = GetMappedValue(mapping, nums[i]);
                indexValues[nums[i]] = i;
            }
            Array.Sort(nums, (a, b) => {
                int comparison = mappedValues[a].CompareTo(mappedValues[b]);
                return comparison != 0 ? comparison : indexValues[a].CompareTo(indexValues[b]);
            });
            return nums;
        }
        

        public int GetMappedValue(int[] mapping, int num)
        {
            if(num == 0)
            {
                return mapping[0];
            }
            int value = 0;
            int pow = 0;
            while (num != 0)
            {
                value += mapping[(num % 10)] * (int)Math.Pow(10, pow);
                pow++;
                num /= 10;
            }
            return value;
        }
    }
}
