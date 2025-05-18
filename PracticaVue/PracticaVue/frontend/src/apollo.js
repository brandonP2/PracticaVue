import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client/core'

const httpLink = createHttpLink({
  uri: 'http://localhost:5001/graphql',
  headers: {
    'Content-Type': 'application/json'
  }
})

const cache = new InMemoryCache()

export default new ApolloClient({
  link: httpLink,
  cache
})