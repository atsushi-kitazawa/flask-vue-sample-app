<template>
  <div class="account">
    <el-table class="data-table" :data="tableData" stripe>
      <el-table-column prop="id" label="Id" width="180"></el-table-column>
      <el-table-column prop="name" label="Name" width="180"></el-table-column>
    </el-table>
  </div>
</template>

<script>
const axios = require('axios').create()
export default {
  name: 'account',
  data () {
    return {
      tableData: []
    }
  },
  mounted () {
    this.updataTableData()
  },
  methods: {
    updataTableData: async function () {
      const response = await axios.get('/api/account')
      this.tableData = response.data
    }
  }
}
</script>

<style scoped>
.data-table {
  width: 80%;
  margin: auto;
}
</style>