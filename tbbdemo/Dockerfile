FROM mcr.microsoft.com/dotnet/sdk:7.0 AS ercanbuild
WORKDIR /app

COPY . .

RUN dotnet restore
RUN dotnet publish --configuration Release -o publish



FROM mcr.microsoft.com/dotnet/aspnet:7.0 

WORKDIR /app

COPY --from=ercanbuild /app/publish .

EXPOSE 80

CMD ["dotnet","tbbdemo.dll"]