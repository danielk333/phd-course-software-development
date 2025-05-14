subroutine fib(a,n)
  integer, intent(in) :: n
  integer, intent(out), dimension(1:n) :: a
  
  do i=1,n
    if (i.eq.1) then
       a(i) = 0
    elseif (i.eq.2) then
       a(i) = 1
    else 
       a(i) = a(i-1) + a(i-2)
    endif
  enddo
end
