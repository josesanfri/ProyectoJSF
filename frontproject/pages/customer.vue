<template>
    <nuxt-child></nuxt-child>
</template>

<script>
import getToken from '~/utils/token/getToken'

export default {
  layout: 'customer/index',
  scrollToTop: true,
  async asyncData(ctx) {
    let {redirect, $axiosAPI, $axiosIntern, store} = ctx

    try {
      let token = await getToken(store)

      if(process.client) {
          await $axiosAPI.get('check/customer/', 
            token ? {
                    'Authorization': token
                } 
                : {}
          ).catch(
            err => redirect('/error/ups/')
          )
      } else {
        await $axiosIntern.get('check/customer/',
          token ? {
                    'Authorization': token
                } 
                : {}
        ).catch(
          err => redirect('/error/ups/')
        )
      }
      
    }
    catch {
       redirect('/error/ups/')
    }
  }
}
</script>
