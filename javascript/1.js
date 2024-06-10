const modifiedArr=new_a.map(num=>{
  if(num<0){
    return Math.abs(num)%26;
  }
})