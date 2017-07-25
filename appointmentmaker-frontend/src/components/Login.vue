<template>
  <ui-form>
    <ui-field placeholder="Username" v-model="username"></ui-field>
    <ui-field placeholder="Password" type="password" v-model="password"></ui-field>
    <button class="ui button" type="submit" @click.prevent="login">Log in</button>
  </ui-form>
</template>

<script>
import {Collections} from 'semantic-ui-vue2';

export default {
  name: 'login',
  mixins: [Collections.Form],
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      this.$auth.login({
        data: {
          username: this.username,
          password: this.password
        },
        success() {
          console.log('success', this.context);
        }
      });
    }
  }
};
</script>
