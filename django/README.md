# Fractal backend

## Start-up
1. `screen`
2. `python3 manage.py runserver 0.0.0.0:8000`
3. `Ctrl+A Ctrl+D`

## API

### Generation request (POST)

1. Endpoint: `fractal/`
2. Data:  
```json
{
  "user": "tomek",
  "name": "mandelbrot",
  "maxIt":200,
  "re":-0.10,
  "im":0.65,
  "h":500,
  "w":500,
  "p1":-1.5,
  "p2":-1.5,
  "k1":1.5,
  "k2":1.5
}
```
## Result preview (GET)
1. PNG endpoint: `preview/?user=tomek`
2. Base64 endpoint: `preview64/?user=tomek`
