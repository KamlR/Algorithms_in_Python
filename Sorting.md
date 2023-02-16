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
