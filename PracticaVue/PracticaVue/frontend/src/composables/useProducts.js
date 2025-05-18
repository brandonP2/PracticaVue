import { useQuery, useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { computed } from 'vue'

const ALL_PRODUCTS = gql`
  query {
    allProducts {
      id
      nombre
      precio
      stock
      disponible
    }
  }
`
const INCREMENT = gql`
  mutation incrementStock($id: Int!) {
    incrementStock(id: $id) {
      ok
      product { id stock disponible }
    }
  }
`
const DECREMENT = gql`
  mutation decrementStock($id: Int!) {
    decrementStock(id: $id) {
      ok
      product { id stock disponible }
    }
  }
`

export function useProducts() {
  const { result, loading, error } = useQuery(ALL_PRODUCTS)
  const productos = computed(() => result.value?.allProducts || [])

  const { mutate: inc } = useMutation(INCREMENT, {
    update(cache, { data: { incrementStock } }) {
      if (!incrementStock.ok) return
      const data = cache.readQuery({ query: ALL_PRODUCTS })
      const updated = data.allProducts.map(p =>
        p.id === incrementStock.product.id ? incrementStock.product : p
      )
      cache.writeQuery({ query: ALL_PRODUCTS, data: { allProducts: updated } })
    }
  })

  const { mutate: dec } = useMutation(DECREMENT, {
    update(cache, { data: { decrementStock } }) {
      if (!decrementStock.ok) return
      const data = cache.readQuery({ query: ALL_PRODUCTS })
      const updated = data.allProducts.map(p =>
        p.id === decrementStock.product.id ? decrementStock.product : p
      )
      cache.writeQuery({ query: ALL_PRODUCTS, data: { allProducts: updated } })
    }
  })

  function incrementarStock(id) {
    inc({ id })
  }
  function disminuirStock(id) {
    dec({ id })
  }

  return { productos, loading, error, incrementarStock, disminuirStock }
}