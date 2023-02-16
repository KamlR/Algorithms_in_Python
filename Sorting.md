## Selection sort:
    void selectionSort(std::vector<int> &nums, int n) {
        int mini;
        for (int i = 0; i < n - 1; ++i) {
            mini = i;
            for (int j = i + 1; j < n; ++j) {
                if (nums[j] < nums[mini]) {
                    mini = j;
                }
            }
            if (mini != i) {
                int temper = nums[i];
                nums[i] = nums[mini];
                nums[mini] = temper;
            }
        }
    }
    
 ## Bubble sort:
     void bubbleSort(std::vector<int> &nums, int n) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n - i - 1; ++j) {
                if (nums[j] > nums[j + 1]) {
                    int temper = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temper;
                }
            }
        }
    }

## Bubble sort Iverson1:
    void bubbleSortIverson1(std::vector<int> &nums, int n) {
        bool flag;
        for (int i = 0; i < n; ++i) {
            flag = false;
            for (int j = 0; j < n - i - 1; ++j) {
                if (nums[j] > nums[j + 1]) {
                    int temper = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temper;
                    flag = true;
                }
            }
            if (!flag) {
                break;
            }
        }
    }
    
## Bubble sort Iverson2:

## Insertion sort:
    void insertionSort(std::vector<int> &nums, int n) {
        int current_num, j;
        for (int i = 1; i < n; ++i) {
            current_num = nums[i];
            j = i - 1;
            while (j >= 0 && nums[j] > current_num) {
                nums[j + 1] = nums[j];
                j -= 1;
            }
            nums[j + 1] = current_num;
        }
    }
## BinaryInsertion sort:
    int binarySearch(int element, int left, int right, std::vector<int> &nums) {
        int middle;
        while (right - left > 1) {
            middle = left + (right - left) / 2;
            if (nums[middle] < element) {
                left = middle;
            } else {
                right = middle;
            }
        }
        return right;
    }
    void binaryInsertionSort(std::vector<int> &nums, int n) {
        int current_num, j;
        for (int i = 1; i < n; ++i) {
            current_num = nums[i];
            j = i - 1;
            int index_loc = binarySearch(current_num, -1, j + 1, nums);
            while (j >= index_loc) {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = current_num;
        }
    }
   
## Counting sort:
    int main() {
        int n, num;
        std::cin >> n;
        std::vector<int> a;
        int maxi;
        for (int i = 0; i < n; ++i) {
            std::cin >> num;
            a.push_back(num);
            if (i == 0) {
                maxi = num;
            } else if (num > maxi) {
                maxi = num;
            }
        }
        std::vector<int> c(maxi + 1);
        for (int i = 0; i < n; ++i) {
            c[a[i]] += 1;
        }
        for (size_t i = 1; i < c.size(); ++i) {
            c[i] = c[i] + c[i - 1];
        }
        std::vector<int> b(n);
        for (int i = n - 1; i >= 0; --i) {
            c[a[i]]--;
            b[c[a[i]]] = a[i];
        }
        for (int i = 0; i < n; ++i) {
            std::cout << b[i] << " ";
        }
    }

## Radix sort:
        #include <iostream>
        #include <vector>
        #include "string"
        #include <algorithm>

        std::vector<int> radix_sort;
        std::vector<int> digits;
        std::vector<int> temper;
        int flag = 0;
        int getDigit(int num, int digit_number) {
            for (int i = 0; i < digit_number; ++i) {
                num /= 256;
            }
            return num % 256;
        }
        void countingSort(int n, int digit_number) {
            if (flag == 0) {
                digits = std::vector<int>(256);
                temper = std::vector<int>(n);
            }
            flag = 1;
            for (int i = 0; i < n; ++i) {
                int index = getDigit(radix_sort[i], digit_number);
                digits[index]++;
            }
            for (int i = 1; i < 256; ++i) {
                digits[i] += digits[i - 1];
            }
            for (int i = n - 1; i >= 0; --i) {
                int index = getDigit(radix_sort[i], digit_number);
                digits[index]--;
                temper[digits[index]] = radix_sort[i];
            }
            for (int i = 0; i < n; ++i) {
                radix_sort[i] = temper[i];
                temper[i] = 0;
            }
            for (int i = 0; i < 256; ++i) {
                digits[i] = 0;
            }
        }
        void radixSort(int n) {
            for (int i = 0; i < 4; ++i) {
                countingSort(n, i);
            }
        }
        int main() {
            int n, x;
            std::cin >> n;
            for (int i = 0; i < n; ++i) {
                std::cin >> x;
                radix_sort.push_back(x);
            }
            radixSort(n);
            for (int i = 0; i < n; ++i) {
                std::cout << radix_sort[i] << " ";
            }
        }
