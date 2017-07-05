main()
{
    int i,j;
    int ip[N][m];
    int hst[NGL];
    for (i=0; i<NGL; i++){
        hst[i]=0;
}

for (j=0; j<N; j++){
   for (i=0; i<M; i++){
       hst[ip[j][i]]++;
   }
}
