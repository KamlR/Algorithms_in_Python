
"""
Класс HashTable реализует хеш-таблицу на основе двумерного списка list.
Разрешение коллизий - метод цепочек.
Расширение - при превышении порога вместимости выполняется рехеширования и увелечение capacity.
"""
class HashTable:
  """Выполянем инициализацию хеш-таблицы."""
  def __init__(self, capacity = 10, load_factor_threshold = 0.8):
    self.capacity = capacity 
    self.size = 0
    self.load_factor_threshold = load_factor_threshold
    self.buckets = [[] for _ in range(self.capacity)] 

  """Вычисляем хеш и получаем индекс для пары <ключ-значение на основе capacity>."""
  def _hash(self, key):
    return hash(key) % self.capacity
  
  """Выполнение рехеширования в случае превышения порога вместимости."""
  def _rehash(self):
    previous_buckets = self.buckets
    self.capacity *= 2

    self.buckets = [[] for _ in range(self.capacity)]
    self.size = 0  

    for bucket in previous_buckets:
      for key, value in bucket:
          self.insert(key, value)

  """Вставка элемента по новому ключу или обновление по уже существующему."""
  def insert(self, key, value):
    index = self._hash(key)
    bucket = self.buckets[index]
    for i in range(len(bucket)):
      if bucket[i][0] == key:
        bucket[i] = (key, value)
        return
    bucket.append((key, value))
    self.size += 1

    if self.size / self.capacity > self.load_factor_threshold:
      self._rehash()

  """Позволяет использовать table[key] = value"""
  def __setitem__(self, key, value):
    self.insert(key, value)

  """
  Удаление элемента по ключу. 
  В случае успешного удаления возвращается value.
  В случае отсутствия переданного ключа выбрасывается исключение.
  """
  def delete(self, key):
    index = self._hash(key)
    bucket = self.buckets[index]

    for i in range(len(bucket)):
      if bucket[i][0] == key:
        value = bucket[i][1] 
        bucket.pop(i)
        self.size-=1
        return value
    raise KeyError
   
  """
  Получение элемента по ключу. 
  В случае отсутствия переданного ключа возвращается None.
  Безопасное получение.
  """
  def get(self, key):
    index = self._hash(key)
    bucket = self.buckets[index]
    for key_, value in bucket:
      if key_ == key:
        return value
    return None
  
  """
  Позволяет использовать print(table[key]).
  Небезопасное получение.
  """
  def __getitem__(self, key):
    result = self.get(key)
    if result == None:
      raise KeyError
    return result
    

  """
  Получение кол-ва элементов.
  """
  def get_size(self):
    return self.size
  
  """
  Вывод всех элементов.
  """
  def print_all_items(self):
    for bucket in self.buckets:
      for key, value in bucket:
        print(key, value)




  


