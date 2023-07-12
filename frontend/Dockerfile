# Use node alpine as it's a small node image
FROM node:alpine

# Create the directory on the node image 
# where our Next.js app will live
RUN mkdir -p /app

# Set /app as the working directory
WORKDIR /app

COPY package*.json /app
COPY next.config.js /app
COPY tsconfig.json /app

# Install dependencies in /app
RUN npm install

COPY src/ .

EXPOSE 3333

CMD npm run dev