# Use an official Node.js image as the base image
FROM node:16

WORKDIR /frontend

# Copy package.json and package-lock.json (or yarn.lock) to install dependencies
COPY package*.json ./

# Install the app dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# # Expose the port that the app will run on (default React port)
# EXPOSE 3000

# Development port
EXPOSE 5173

# Set the environment to production
# ENV NODE_ENV=production
ENV NODE_ENV=development

# # Build the app for production
# RUN npm run build

# # Start the app
# CMD ["npm", "start"]

# Start the app in development mode
CMD ["npm", "run", "dev"]
