data Box:
  | box(ref v)
end

fun mk-counter():
  ctr = box(0)
  lam():
    ctr!{v : (ctr!v + 1)}
    ctr!v
  end
where: 
  l1 = mk-counter()
  l1() is 1
  l1() is 2
  l2 = mk-counter()
  l2() is 1
  l1() is 3
  l2() is 2
end

fun mk-counter-var():
  var ctr = 0
  lam():
    ctr := ctr + 1
    ctr
  end
where: 
  l1 = mk-counter-var()
  l1() is 1
  l1() is 2
  l2 = mk-counter-var()
  l2() is 1
  l1() is 3
  l2() is 2
end