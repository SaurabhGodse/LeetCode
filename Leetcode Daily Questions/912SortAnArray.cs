using System;

namespace Leetcode_Daily_Questions
{
    public class _912SortAnArray
    {
        public static void Main(string[] args)
        {
            _912SortAnArray sortAnArray = new _912SortAnArray();
            int[] nums = { 5, 2, 3, 1 };
            sortAnArray.Print(sortAnArray.SortArray(nums));
        }
        public int[] SortArray(int[] nums)
        {
            /*
             * In this we are sorting the array using Three-Way Partitioning
             * This method is particularly useful when dealing with arrays containing many duplicate elements. It partitions the array into three parts:
                1. Elements less than the pivot
                2. Elements equal to the pivot
                3. Elements greater than the pivot
             */
            QuickSort(nums, 0, nums.Length - 1);
            return nums;
        }

        public void QuickSort(int[] nums, int low, int high)
        {
            if (low < high)
            {
                var bounds = Partition(nums, low, high);
                QuickSort(nums, low, bounds.lt - 1);
                QuickSort(nums, bounds.gt + 1, high);
            }
        }
        public (int lt, int gt) Partition(int[] nums, int low, int high)
        {
            int pivot = nums[low];
            int lt = low;
            int i = low + 1;
            int gt = high;
            while (i <= gt)
            {
                if (nums[i] < pivot)
                {
                    Swap(nums, i++, lt++);
                }
                else if (nums[i] > pivot)
                {
                    Swap(nums, i, gt--);
                }
                else
                {
                    i++;
                }
            }
            return (lt, gt);
        }
        public void Swap(int[] nums, int a, int b)
        {
            int temp = nums[a];
            nums[a] = nums[b];
            nums[b] = temp;
        }

        private void Print(int[] nums)
        {
            foreach(int i in nums)
            {
                Console.WriteLine(i);
            }
        }
    }
}
