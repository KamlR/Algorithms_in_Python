### Разложение на простые множители
    std::vector<int> factorization(int x) {
        std::vector<int> answer;
        if (x == 1) {
            answer.push_back(1);
            return answer;
        }
        answer.push_back(1);
        int sqr = sqrt(x);
        int factor = 2;
        while (factor <= sqr) {
            if (x % factor == 0) {
                x /= factor;
                answer.push_back(factor);
                while (x % factor == 0) {
                    x /= factor;
                    answer.push_back(factor);
                }
                sqr = sqrt(x);
            }
            factor += 1;
        }
        if (x > 1) {
            answer.push_back(x);
        }
        return answer;
    }
