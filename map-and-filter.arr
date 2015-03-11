fun my-map<A,B>(func :: (A -> B), l :: List<A>) -> List<B>:
  cases(List<A>) l:
    | empty => empty
    | link(f, r) =>
      link(func(f), map(func, r))
  end
where:
  my-map(_.first, [list: [list: 1], [list: 2]]) is [list: 1, 2]
  my-map(string-toupper, [list: "one", "two"]) is [list: "ONE", "TWO"]
end

fun my-filter<A>(func :: (A -> Boolean), l :: List<A>) -> List<A>:
  cases(List<A>) l:
    | empty => empty
    | link(f, r) =>
      if func(f):
        link(f, my-filter(func, r))
      else:
        my-filter(func, r)
      end
  end
  
where:
  filter(_ > 1, [list: 1, 2, 3]) is [list: 2, 3]
end
