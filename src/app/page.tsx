import { Card } from '@nextui-org/card'
export default function Home() {
  return (
    <div className="space-y-10">
      <div className="grid grid-cols-4 gap-10">
        <Card className="h-[200px] bg-primary "></Card>
        <Card className="h-[200px]"></Card>
        <Card className="h-[200px]"></Card>
        <Card className="h-[200px]"></Card>
      </div>
      <div className="grid grid-cols-3 gap-10">
        <Card className="h-[300px]"></Card>
        <Card className="h-[300px]"></Card>
        <Card className="h-[300px]"></Card>
      </div>
      <Card className="w-full h-[500px]"></Card>
    </div>
  )
}
